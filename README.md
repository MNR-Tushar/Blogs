# LearnLog - Django Blog Platform

A full-featured blog website built with Django 5.2.4, featuring user authentication, blog management, comments, tags, categories, and social features like following other users.

## Features

### User Management
- **Custom User Model** with profile pictures
- User registration and authentication
- Profile management (update info, change password, profile picture)
- Follow/Unfollow system
- User information pages showing posts and followers

### Blog Features
- **Rich Text Editor** integration with CKEditor
- Create, read, update, and delete blog posts
- Blog banners/images
- Categories and tags system
- Search functionality (by title, category, author, tags)
- Comment system with nested replies
- Like system for posts
- Pagination for blog listings
- Related posts suggestions

### Navigation & Organization
- Home page with featured blog carousel
- Blog listing page with pagination
- Category-based filtering
- Tag-based filtering
- Search functionality
- Sidebar with recent posts, categories, and tag clouds

## Technology Stack

- **Backend**: Django 5.2.4
- **Database**: SQLite3 (development)
- **Rich Text Editor**: django-ckeditor 6.7.3
- **Image Processing**: Pillow 11.3.0
- **Frontend**: Bootstrap, jQuery, Owl Carousel
- **Authentication**: Django built-in auth system

## Installation

1. **Clone the repository**
```bash
git clone <your-repo-url>
cd blog_website
```

2. **Create a virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Run migrations**
```bash
python manage.py migrate
```

5. **Create a superuser**
```bash
python manage.py createsuperuser
```

6. **Collect static files**
```bash
python manage.py collectstatic
```

7. **Run the development server**
```bash
python manage.py runserver
```

8. Visit `http://127.0.0.1:8000/` in your browser

## Project Structure

```
blog_website/
├── blog_website/          # Project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── blogs/                 # Blog app
│   ├── models.py         # Blog, Category, Tags, Comment, Reply models
│   ├── views.py          # Blog views
│   ├── forms.py          # Blog forms
│   └── urls.py
├── user_profile/         # User management app
│   ├── models.py         # Custom User and Follow models
│   ├── views.py          # Auth and profile views
│   ├── forms.py          # User forms
│   └── managers.py       # Custom user manager
├── templates/            # HTML templates
├── assets/              # Static files (CSS, JS, images)
└── media/               # User uploaded files
```

## Key Models

### User
- Extended from Django's AbstractUser
- Additional fields: `profile_image`, `followers`
- Custom manager for user creation

### Blog
- Fields: `title`, `slug`, `banner`, `description`, `category`, `tags`, `user`, `like`
- Auto-generates slug from title
- Rich text description using CKEditor

### Category
- Simple categorization for blogs
- Auto-generates slug

### Tags
- Many-to-many relationship with blogs
- Auto-generates slug

### Comment & Reply
- Hierarchical comment system
- Comments on blogs, replies on comments

### Follow
- User following system
- Track followers and following relationships

## Configuration

### Debug Mode
Currently set to `DEBUG = False` for production. For development, change in `settings.py`:
```python
DEBUG = True
```

### Allowed Hosts
```python
ALLOWED_HOSTS = ["localhost", "127.0.0.1", "learnlog.pythonanywhere.com"]
```

### Media Files
- Media files are stored in `media/` directory
- Profile images: `media/profile_images/`
- Blog banners: `media/blog_banners/`

## Admin Panel

Access the admin panel at `/admin/` with your superuser credentials to:
- Manage users
- Create/edit categories and tags
- Moderate blogs and comments
- View follow relationships

## URL Routes

### Main Routes
- `/` - Home page
- `/blogs/` - All blogs with pagination
- `/blog_details/<slug>/` - Individual blog post
- `/search_blogs/` - Search results
- `/category_blogs/<slug>/` - Category-filtered blogs
- `/tag_blogs/<slug>/` - Tag-filtered blogs

### User Routes
- `/login/` - User login
- `/register/` - User registration
- `/logout/` - User logout
- `/profile/` - User profile management
- `/my_blogs/` - User's own blogs
- `/add_blog/` - Create new blog
- `/update_blog/<slug>/` - Edit blog
- `/view_user_information/<username>/` - Public user profile

## Usage

### Creating a Blog Post

1. Login to your account
2. Navigate to "Add Blog" from your profile
3. Fill in the blog details:
   - Title
   - Category
   - Description (with rich text formatting)
   - Banner image
   - Tags (comma-separated)
4. Click "Add" to publish

### Managing Your Blogs

1. Go to "My Blogs" from your profile
2. View all your published blogs
3. Edit or delete any blog post
4. Track comments and engagement

### Following Users

1. Visit any user's profile by clicking their username
2. Click "Follow" to follow them
3. View their posts and updates
4. Unfollow anytime from their profile

## Deployment Notes

The project is configured for deployment on PythonAnywhere:
- Static files served from `/static/`
- Media files served from `/media/`
- SECRET_KEY should be moved to environment variables for production
- Database should be upgraded to PostgreSQL for production

## Security Considerations

⚠️ **Important**: Before deploying to production:
1. Change the SECRET_KEY in settings.py
2. Set DEBUG = False
3. Configure proper ALLOWED_HOSTS
4. Use environment variables for sensitive data
5. Set up HTTPS
6. Configure proper CSRF settings

## Troubleshooting

### Common Issues

**Issue**: Static files not loading
```bash
python manage.py collectstatic --clear
```

**Issue**: Database errors
```bash
python manage.py migrate --run-syncdb
```

**Issue**: CKEditor not appearing
- Ensure `{{form.media}}` is in your template
- Check that static files are properly configured

## Future Enhancements

- [ ] Email notifications for comments
- [ ] Blog post drafts
- [ ] Social media sharing
- [ ] Blog post scheduling
- [ ] Advanced analytics
- [ ] Multiple image uploads per blog
- [ ] Video embedding support
- [ ] Export blogs to PDF

## Contributing

Feel free to submit issues and enhancement requests!

## License

Copyright 2025 - All rights reserved

## Contact

- Facebook: [mdnaimurrahman36](https://www.facebook.com/mdnaimurrahman36/)
- LinkedIn: [mdnaimurrahman36](https://www.linkedin.com/in/mdnaimurrahman36/)

---

Built with ❤️ using Django
