# Production
In `frontend/src/components/Map.vue` add Mapbox accessToken:
```javascript
...
  data() {
    return {  
      accessToken: "",
      mapStyle: "mapbox://styles/mapbox/streets-v11",
...
```

```bash
# install dependencies
npm install
pip install -r requirements.txt

# build for production
npm run build

# apply migrations
python manage.py migrate

# collect static files into STATIC_ROOT
python manage.py collectstatic

# start server
python manage.py runserver
```
