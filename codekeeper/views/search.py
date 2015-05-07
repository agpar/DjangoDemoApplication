from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from codekeeper import settings
from rest_framework.renderers import JSONRenderer
import scorched

from codekeeper.serializers.search import SearchSerializer
from codekeeper.renderers.custom_html_renderer import CustomHTMLRenderer


class SearchViewHTMLRenderer(CustomHTMLRenderer):
    template_name = "search/search.html"


class SearchView(GenericAPIView):
    serializer_class = SearchSerializer
    renderer_classes = (JSONRenderer, SearchViewHTMLRenderer)

    def get(self, request, *args, **kwargs):
        querydict = request.GET
        if not querydict:
            return Response({"results": []})

        solrconn = scorched.SolrInterface(settings.SOLR_SERVER)
        solrResp = solrconn.query(text=querydict.get('q')).facet_by(fields=["type", "first_name", "tags"]).execute()
        serialized_response = self.get_serializer(solrResp)
        return Response({'search_results': serialized_response.data})