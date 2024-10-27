source "/Users/songye03/Desktop/me/.venv/bin/activate"
python "/Users/songye03/Desktop/me/_site/travelmap.py"
cd "/Users/songye03/Desktop/me"
git add .
git commit -m "update travelmap"
git push
bundle exec jekyll clean
lsof -i :4000
bundle exec jekyll serve
