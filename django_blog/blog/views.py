from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages #show success/error messages
from .forms import SignUpForm, UserUpdateForm
from django.views.generic import ListView,CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.db.models import Q # Import Q objects for complex lookups
# Import reverse_lazy to handle redirects after a successful deletion
from django.urls import reverse_lazy
#Registration View
def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account for {username} has been created. You can now log in.')
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'blog/register.html', {'form':form})
    
#Profile View
@login_required
def profile(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated.')
            return redirect('profile')
    else:
        form = UserUpdateForm(instance=request.user)
    return render(request, 'blog/profile.html', {'form':form})


def home(request):
    return render(request, 'blog/home.html')

class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    ordering = ['-published_date']

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('post_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('post_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        #Get the specific post object being accessed
        post = self.get_object()
        #Return True only if the current user is the author of the post
        if self.request.user == post.author:
            return True
        return False
    
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('post_list')

    def test_func(self):
        #Ensure only the author can delete their own post
        post = self.get_object()
        return self.request.user == post.author
    
# class CommentListView(ListView):
#     model = Comment
#     template_name = 'blog/post_detail.html'
#     context_object_name = 'comments'
#     ordering = ['-created_at']

class CommentCreateView(LoginRequiredMixin,CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comment_form.html'

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    # Redirect to the post detail page on success
    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'pk': self.kwargs['pk']})
    
class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comment_form.html'
    
    def test_func(self):
        #Ensure only the author can edit their own comment
        comment = self.get_object()
        return self.request.user == comment.author
    
    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'pk': self.kwargs['pk']})

    
class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = 'blog/comment_confirm_delete.html'

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author
    
    def get_success_url(self):
        # We need the post ID to redirect back to the right page
        comment = self.get_object()
        return reverse_lazy('post_detail', kwargs={'pk': comment.post.pk})
    
# View to display posts filtered by a specific tag
class PostByTagListView(ListView):
    model = Post
    template_name = 'blog/post_list.html' # Reuse the existing list template
    context_object_name = 'posts'
    ordering = ['-published_date']

    def get_queryset(self):
        # Retrieve the tag slug from the URL parameters
        tag_slug = self.kwargs.get('tag_slug')
        # Filter posts where tags__slug matches the URL tag
        return Post.objects.filter(tags__slug=tag_slug).order_by('-published_date')

#To handle search functionality
def search_posts(request):
    query = request.GET.get('q') # Get the search term from the URL (e.g., ?q=django)
    results = []

    if query:
        results = Post.objects.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(tags__name__icontains=query)
        ).distinct() #ensures we don't get duplicate posts if multiple fields match

    return render(request, 'blog/search_results.html', {'results': results, 'query': query})
    


    

