from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name="project name")
    description = models.TextField(verbose_name="information")
    image = models.ImageField(
        upload_to="portfolio/",
        verbose_name="project picture"
    )
    technologies = models.CharField(
        max_length=300,
        verbose_name="technology"
    )
    github_url = models.URLField(blank=True, verbose_name="github link")
    live_url = models.URLField(blank=True, verbose_name="online link")
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True, verbose_name="visible on website")

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "portfolio"
        verbose_name_plural = "portfolios"

    def __str__(self):
        return self.title
