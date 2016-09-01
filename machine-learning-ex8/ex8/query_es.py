#!/usr/local/bin/python3.3

from elasticsearch import Elasticsearch

params = {'cluster_nodes' : ['172.31.22.169:9200'], 'index' : 'factual_index', 'type': 'factual_type'}

def get_es_connection(params):
	"""Fetch a connection to the factual index"""
	cluster_nodes = params['cluster_nodes']
	index = params['index']
	es_connection = Elasticsearch(cluster_nodes, index=index, sniff_on_start=False, sniff_on_connection_fail=False, timeout=30)
	return es_connection

def get_qs_connection(term, field_list=None):
	"""Return a "query_string" style ElasticSearch query object"""
	if field_list is None:
		field_list = []
	return {
		"query_string": {
			"query": term,
			"fields": field_list
		}
	}

def search_index(term):
	qs = get_qs_connection(term, ['name'])
	index = params['index']
	es = get_es_connection(params)
	result = es.search(index=index, body={"query": qs})
	if 'hits' not in result or result['hits']['total'] == 0:
		return 'no search result'

	hits = result['hits']['hits']
	top_hit = hits[0]
	return top_hit["_source"].get('name', '')


if __name__ == '__main__':
	print(search_index("silver state school"))