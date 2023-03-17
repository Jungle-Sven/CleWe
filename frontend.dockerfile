FROM node:18-alpine as builder

# set the working dir for container
WORKDIR /frontend

COPY ui /frontend

RUN npm install

RUN npm install -g pnpm


RUN pnpm install

EXPOSE 3000

RUN pnpm run build

CMD ["pnpm", "start"]
