class ValidateModelMixin(object):

    def save(self, *args, **kwargs):
        self.full_clean()
        super(ValidateModelMixin, self).save(*args, **kwargs)
