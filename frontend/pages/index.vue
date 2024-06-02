<template>
    <div class="mt-5 flex flex-col items-center justify-center">
        <form class="mt-5 flex flex-row items-center justify-center space-x-4" @submit.prevent="uploadImage">
        <div class="flex items-center justify-center space-x-4">
            <div class="flex items-center justify-center h-full w-60">
            <label for="dropzone-file" class="flex flex-col items-center justify-center border-2 h-60 w-60 border-gray-300 border-dashed rounded-full cursor-pointer bg-gray-50  hover:bg-gray-100">
                <div v-if="!image" class="flex flex-col items-center justify-center pt-5 pb-6">
                <svg class="w-8 h-8 mb-4 text-gray-500 " aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 20 16">
                    <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 13h3a3 3 0 0 0 0-6h-.025A5.56 5.56 0 0 0 16 6.5 5.5 5.5 0 0 0 5.207 5.021C5.137 5.017 5.071 5 5 5a4 4 0 0 0 0 8h2.167M10 15V6m0 0L8 8m2-2 2 2"/>
                </svg>
    
                <p class="mb-2 text-sm text-gray-500">Click to upload</p>
                </div>
                
                <img v-else :src="image" class="h-60 w-60 rounded-full object-cover">
    
                <input ref="files" id="dropzone-file" type="file" class="hidden" @change="onFileChange" />
            </label>
            </div>
            
        </div>
    
        <button class="max-w-fit bg-blue-600 text-white rounded px-4 py-2 font-medium">Upload image</button>
        </form>

        <div v-if="loading" class="mt-4" role="status">
            <svg aria-hidden="true" class="w-20 h-20 text-gray-200 animate-spin dark:text-gray-600 fill-blue-600" viewBox="0 0 100 101" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M100 50.5908C100 78.2051 77.6142 100.591 50 100.591C22.3858 100.591 0 78.2051 0 50.5908C0 22.9766 22.3858 0.59082 50 0.59082C77.6142 0.59082 100 22.9766 100 50.5908ZM9.08144 50.5908C9.08144 73.1895 27.4013 91.5094 50 91.5094C72.5987 91.5094 90.9186 73.1895 90.9186 50.5908C90.9186 27.9921 72.5987 9.67226 50 9.67226C27.4013 9.67226 9.08144 27.9921 9.08144 50.5908Z" fill="currentColor"/>
                <path d="M93.9676 39.0409C96.393 38.4038 97.8624 35.9116 97.0079 33.5539C95.2932 28.8227 92.871 24.3692 89.8167 20.348C85.8452 15.1192 80.8826 10.7238 75.2124 7.41289C69.5422 4.10194 63.2754 1.94025 56.7698 1.05124C51.7666 0.367541 46.6976 0.446843 41.7345 1.27873C39.2613 1.69328 37.813 4.19778 38.4501 6.62326C39.0873 9.04874 41.5694 10.4717 44.0505 10.1071C47.8511 9.54855 51.7191 9.52689 55.5402 10.0491C60.8642 10.7766 65.9928 12.5457 70.6331 15.2552C75.2735 17.9648 79.3347 21.5619 82.5849 25.841C84.9175 28.9121 86.7997 32.2913 88.1811 35.8758C89.083 38.2158 91.5421 39.6781 93.9676 39.0409Z" fill="currentFill"/>
            </svg>
            <span class="sr-only">Loading...</span>
        </div>

        <span v-if="res" class="text-green-600 font-medium">Results:</span>
        <div class="mt-4 w-full flex flex-col items-center justify-center space-y-4">
            <canvas class="max-w-[50%]" ref="canvasEl"/>
        </div>

        <span v-if="error" class="text-red-600 font-medium">{{ error }}</span>

    </div>
  </template>
  
  <script setup lang="ts">
    const runtimeConfig = useRuntimeConfig();

    console.log(runtimeConfig.public.backend_host);
    const files = ref();
    const image = ref();
    const res = ref();
    const error = ref();
    const loading = ref();
    const formData = ref(new FormData());
    const canvasEl: Ref<HTMLCanvasElement | undefined> = ref();
    
    function onFileChange(e: Event) {
        const el = (e.target as HTMLInputElement);
        const file = el?.files ? el?.files[0] : null;
        if (file !== null) {
            image.value = URL.createObjectURL(file);
        }
    }
    
    async function uploadImage() {
    try {
        loading.value = true;
        let uploadedImage: HTMLImageElement | undefined;
        error.value = null;
        res.value = null;
        Array.from(files.value.files).map((file, _) => {
            formData.value.append("file", file as File);
            uploadedImage = new Image();
            uploadedImage.src = image.value;
        });

        const response: Result[] = await $fetch<Result[]>(`${runtimeConfig.public.backend_host}/server/detect/7ed8fd3c-2da8-40f9-bfa4-a0602a00e217/`, {
        method: 'POST',
        body: formData.value,
        });

        res.value = response;

        if (uploadedImage !== null && uploadedImage !== undefined && canvasEl.value != null) {
            const ctx = canvasEl.value.getContext('2d');
            canvasEl.value.width = uploadedImage.width;
            canvasEl.value.height = uploadedImage.height;
            ctx?.drawImage(uploadedImage, 0, 0);

            if (ctx !== null) {
                response.forEach((result) => {
                    ctx.strokeStyle = 'blue';
                    ctx.lineWidth = 2;
                    ctx.strokeRect(result.box.x1, result.box.y1, result.box.x2 - result.box.x1, result.box.y2 - result.box.y1);
                    ctx.fillStyle = 'blue';
                    ctx.fillText(result.name, result.box.x1, result.box.y1 - 4);
                })
            }
        }

    } catch (e) {
        error.value = (e as Error).message;
    }
    loading.value = false;
    }

    interface Box {
        x1: number,
        x2: number,
        y1: number,
        y2: number
    }

    interface Result {
        name: string,
        class: number,
        confidence: number,
        box: Box
    }
  </script>