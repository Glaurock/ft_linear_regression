# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: gmonnier <gmonnier@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/11/16 20:22:14 by gmonnier          #+#    #+#              #
#    Updated: 2018/11/16 20:31:05 by gmonnier         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

all:
	@printf "No compilation for python yet...\\n"

learning:
	python3 src/learning.py resources/data.csv

predict:
	python3 src/predict.py resources/data.csv

accuracy:
	python3 src/accuracy.py resources/data.csv

clean:
	rm -rf __pycache__
	rm -rf src/__pycache__/
