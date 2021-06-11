# TODO productionize
# pull official base image
FROM node:13.12.0-alpine

# set working directory
WORKDIR /usr/src/networthtracker-ui

# add `/app/node_modules/.bin` to $PATH
ENV PATH /usr/src/networthtracker-ui/node_modules/.bin:$PATH

# install app dependencies
COPY package.json ./
COPY package-lock.json ./
RUN npm install
RUN npm install react-scripts@3.4.1 -g

# add app
COPY . ./

# start app
CMD ["npm", "start"]
