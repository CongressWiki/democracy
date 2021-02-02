FROM node:current-alpine AS base
WORKDIR /base
COPY package.json ./
COPY yarn.lock ./
RUN yarn install --pure-lockfile
# TODO add --ignore-scripts
COPY . .
RUN git clone https://github.com/unitedstates/images.git ./public/elected_officials

FROM base AS build
ENV NODE_ENV=production
ENV NEXT_TELEMETRY_DISABLED=1
WORKDIR /build
COPY --from=base /base ./
RUN yarn build

FROM node:current-alpine AS production
ENV NODE_ENV=production
ENV NEXT_TELEMETRY_DISABLED=1
WORKDIR /app
COPY --from=build /build/node_modules ./node_modules
COPY --from=build /build/package.json ./
COPY --from=build /build/yarn.lock ./
COPY --from=build /build/.next ./.next
COPY --from=build /build/public ./public

EXPOSE 3000

CMD yarn start