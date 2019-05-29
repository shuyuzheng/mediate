from flask import render_template, request, redirect, flash, url_for
from app.forms import SearchForm
from app.apis import get_movies, get_info
from app import app

@app.route('/')
@app.route('/search', methods=['GET', 'POST'])
def search():
    form = SearchForm()
    if form.validate_on_submit():
        flash('Success search')
        data = {'query': form.query.data, 
                'order': form.order.data,
                'reviewer': form.reviewer.data}
        if form.publication_start.data is not None:
            if form.publication_end.data is not None:
                data.update({'publication-date': form.publication_start.data + ';' + form.publication_end.data})
            else:
                data.update({'publication-date': form.plulication_start})

        if form.opening_start.data is not None:
            if form.opening_end.data is not None:
                data.update({'opening-date': form.opening_start.data + ';' + form.opening_end.data})
            else:
                data.update({'opening-date': form.opening_start.data})

        if form.critics_pick.data:
            data.update({'critics-pick': 'Y'})

        query = {k:v for k,v in data.items() if data[k] is not None}
        movies = get_movies(query)
        return render_template('result.html', title='Result', movies=movies)
    return render_template('search.html', title='Search', form=form)

@app.route('/detail/<moviename>')
def detail(moviename):
    infos = get_info(moviename)
    return render_template('detail.html', title='Detail', infos=infos)
