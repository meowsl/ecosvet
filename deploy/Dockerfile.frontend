FROM node:18-alpine

WORKDIR /var/www/app

# install global packages
RUN apk update \
    && apk upgrade \
    && apk add --no-cache  \
    yarn

# install frontend packages
COPY package.json package.json
COPY yarn.lock yarn.lock
RUN npm install -g @quasar/cli
RUN set -ex && yarn

COPY . .

RUN yarn build
