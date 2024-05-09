FROM php:8.2-apache

RUN rm /bin/sh && ln -s /bin/bash /bin/sh

RUN apt-get update
RUN apt-get install -y git curl zip zlib1g zlib1g-dev libzip-dev libpng-dev\
  unzip nodejs npm

COPY ./configD/vhost.conf /etc/apache2/sites-enabled/000-default.conf
COPY . /var/www
COPY ./configD/env /var/www/.env

RUN docker-php-ext-install mysqli pdo pdo_mysql gd zip
RUN docker-php-ext-enable mysqli pdo pdo_mysql

RUN curl -sS https://getcomposer.org/installer \
  | php -- --install-dir=/usr/local/bin --filename=composer

RUN a2enmod rewrite

RUN mkdir -p /var/www/data \
  && mkdir -p /var/www/data/cache

RUN chown www-data:www-data -R /var/www/bootstrap/cache\
  &&chown www-data:www-data -R /var/www/storage\
  &&chown www-data:www-data -R /var/www/public\
  &&chown www-data:www-data -R /var/www/data

WORKDIR /var/www

RUN composer install