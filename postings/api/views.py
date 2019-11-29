from rest_framework import generics,mixins
from postings.models import BlogPost
from .serializers import BlogPostSerializer
from .permissions import IsOwnerOrReadOnly


class BlogRudAPIView(mixins.CreateModelMixin,generics.ListAPIView):
    lookup_field='pk'
    serializer_class=BlogPostSerializer
    

    def get_queryset(self):
        qs=BlogPost.objects.all()
        query=self.request.GET.get('q')
        if query is not None:
            qs=qs.filter(Q(title_icontains=query)|Q(content_icontains=query)).distinct()
        return qs
    def perform_create(self,serializer):
        serializer.save(user=self.request.user)
    def post(self,request,*args,**kwargs):# for Post method
        return seld.create(request,*args,**kwargs)
    def put(self,request,*args,**kwargs):# for Post method
        return seld.update(request,*args,**kwargs)
    def patch(self,request,*args,**kwargs):# for Post method
        return seld.update(request,*args,**kwargs)





# class BlogRudAPIView(generics.CreateAPIView):
#     lookup_field='pk'
#     serializer_class=BlogPostSerializer

#     def get_queryset(self):
#         return BlogPost.objects.all()
#     def perform_create(self,serializer):
#         serializer.save(user=self.request.user)

class BlogPostRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field='pk'
    serializer_class=BlogPostSerializer
    permission_class=[IsOwnerOrReadOnly]

    def get_queryset(self):
        return BlogPost.objects.all()
