FROM node:alpine

# copy source files
COPY LICENSE LICENSE
COPY components components
COPY lib lib
COPY pages pages
COPY posts posts
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