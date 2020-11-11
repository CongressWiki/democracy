FROM node:alpine

# copy source files
COPY components components
COPY pages pages
COPY public public
COPY styles styles
COPY next-env.d.ts next-env.d.ts
COPY tsconfig.json tsconfig.json
COPY package.json package.json
COPY yarn.lock yarn.lock

# install dependencies
RUN yarn

# start app
RUN yarn build
CMD yarn start