import profeco_json
import web

profeco = profeco_json.Profeco_json()
profeco.data_read('data.json')

render = web.template.render('views/')

urls = ('/','index',
        '/mapa','mapa',
        '/data(.*)','data'
        )

class index:
    def GET(self):
        return render.index()
class data:
    def GET(self,data):
        data = profeco.data_get_data()
        return render.data(data)
class mapa:
    def GET(self):
        return render.mapa()

if __name__ == '__main__':
    app = web.application(urls, globals())
    web.config.debug = True
    app.run()

