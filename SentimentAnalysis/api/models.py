from django.db import models
from chatbot.forms import SentimentForm
from django import forms

class FeedList(models.Model):
    id                      = models.AutoField(primary_key=True)
    #tenant                  = models.forms(SentimentForm, on_delete=models.CASCADE)
    #member                  = models.ForeignKey(MembersList, on_delete=models.CASCADE)
    description             = models.TextField(blank=True, null=True)
    community_id            = models.IntegerField(blank=True, null=True, default=0)
    post_type               = models.IntegerField(blank=True, null=True, default=0) # 1 -> Private 0 -> Public,  // Public=0 or Community = 1
    member_type             = models.CharField(max_length=500, blank=True, null=True)
    allow_share             = models.IntegerField(blank=True, null=True, default=0)
    url_link                = models.CharField(max_length=500, blank=True, null=True)
    url_meta_title          = models.CharField(max_length=500, blank=True, null=True)
    url_meta_description    = models.CharField(max_length=500, blank=True, null=True)
    url_preview_image       = models.CharField(max_length=500, blank=True, null=True)
    content_type            = models.CharField(max_length=500, blank=True, null=True) # post / profilepic / coverpic
    content_id              = models.IntegerField(blank=True, null=True, default=0)
    allow_comments          = models.IntegerField(blank=True, null=True, default=1)
    attachment_type         = models.CharField(max_length=500, blank=True, null=True) # images / videos / attachment
    tenant_source           = models.CharField(max_length=500, blank=True, null=True)
    tenant_source_id        = models.IntegerField(blank=True, null=True, default=0)
    draft_status            = models.IntegerField(blank=True, null=True, default=0)
    archive_status          = models.IntegerField(blank=True, null=True, default=0)
    visibility              = models.IntegerField(blank=True, null=True, default=1)
    delete_status           = models.IntegerField(blank=True, null=True, default=0)
    created_at              = models.BigIntegerField(blank=True, null=True)
    updated_at              = models.BigIntegerField(blank=True, null=True)
    class Meta:
        db_table = 'post_tbl'
        ordering = ['id']
