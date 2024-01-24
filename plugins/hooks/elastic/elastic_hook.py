from airflow.plugins_manager import AirflowPlugin
from airflow.hooks.base import BaseHook

from elasticsearch import Elasticsearch

class ElasticHook(BaseHook):
    def __init__(self, conn_id='elastic_default', *args, **kwargs):
        super().__init__(*args, **kwargs)
        con = self.get_connection(conn_id)

        cfg = {}
        hosts = []

        if con.host:
            hosts = con.host.split(',')
        if con.port:
            cfg['port'] = int(con.port)
        if con.login:
            cfg['http_auth'] = (con.login, con.password)
        
        self.es = Elasticsearch(hosts, **cfg)
        self.index = con.schema

    def info(self):
        return self.es.info()

    def set_index(self, index):
        self.index = index

    def add_doc(self, index, doc_type, doc):
        self.set_index(index)
        return self.es.index(index=index, doc_type=doc_type, doc=doc)
    
class AirflowElasticPlugin(AirflowPlugin):
    name = 'elastic'
    hooks = [ElasticHook]