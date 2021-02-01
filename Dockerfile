FROM node:alpine

# copy source files
COPY components components
COPY pages pages
COPY public public
COPY libs libs
COPY top-layer-layout top-layer-layout
COPY .babelrc .babelrc
COPY next-env.d.ts next-env.d.ts
COPY next.config.js next.config.js
COPY tsconfig.json tsconfig.json
COPY package.json package.json
COPY yarn.lock yarn.lock

# install dependencies
RUN yarn --pure-lockfile

# Build app
RUN yarn build

# Start app
CMD yarn start