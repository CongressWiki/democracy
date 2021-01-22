FROM node:alpine

# copy source files
COPY components components
COPY pages pages
COPY public public
COPY lib lib
COPY top-layer-layout top-layer-layout
COPY .babelrc .babelrc
COPY next-env.d.ts next-env.d.ts
COPY tsconfig.json tsconfig.json
COPY package.json package.json
COPY yarn.lock yarn.lock

# install dependencies
RUN yarn --pure-lockfile

# start app
RUN yarn build
CMD yarn start