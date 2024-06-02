FROM node:21-slim as build
ENV NODE_ENV=production
WORKDIR /src
COPY . .
RUN npm install
RUN npm run build
RUN npm prune

FROM build
COPY --from=build /src/.output /src/.output
CMD ["node", ".output/server/index.mjs"]
