"""Mixins for testing models from post app"""

def test_parameter_of_field(model, self_,
                            field_and_parameter: dict,
                            parameter_name: str):
    """Test field's parameter of all model's objects"""

    for object_ in model.objects.all():
        for field, expected_parameter in field_and_parameter.items():
            error_message = f'{parameter_name} for {field} in {model.__name__}'

            with self_.subTest(error_message):
                real_parameter = getattr(
                    object_._meta.get_field(field), parameter_name
                )

                self_.assertEqual(real_parameter, expected_parameter)


class TestVerboseNameMixin:
    """Mixin with function for testing verbose_name parameter"""

    def test_verbose_name(self, model):
        """Test verbose_name parameter for fields"""

        test_parameter_of_field(
            model, self, self.field_and_verbose_name, 'verbose_name'
        )


class TestAutoNowAddMixin:
    """Mixin with function for testing auto_now_add parameter"""

    def test_auto_now_add(self, model):
        """Test auto_now_add parameter for fields"""

        for object_ in model.objects.all():
            for field in self.auto_now_add_fields:
                auto_now_add_value = \
                    object_._meta.get_field(field).auto_now_add

                self.assertTrue(auto_now_add_value)


class TestMaxLengthMixin:
    """Mixin with function for testing max_length parameter"""

    def test_max_length(self, model):
        """Test max_length parameter for fields"""

        test_parameter_of_field(
            model, self, self.field_and_max_length, 'max_length'
        )


class TestDbIndexMixin:
    """Mixin with function for testing db_index parameter"""

    def test_db_index(self, model):
        """Test db_index parameter for fields"""

        for object_ in model.objects.all():
            for field in self.db_index_fields:
                db_index_value = object_._meta.get_field(field).db_index

                self.assertTrue(db_index_value)


class TestAutoNowMixin:
    """Mixin with function for testing auto_now parameter"""

    def test_auto_now(self, model):
        """Test auto_now parameter for fields"""

        for object_ in model.objects.all():
            for field in self.auto_now_fields:
                auto_now_value = object_._meta.get_field(field).auto_now

                self.assertEqual(auto_now_value, True)


class TestChoicesMixin:
    """Mixin with function for testing choices parameter"""

    def test_choices(self, model):
        """Test choices parameter for fields"""

        test_parameter_of_field(
            model, self, self.field_and_choices, 'choices'
        )


class TestBlankMixin:
    """Mixin with function for testing blank parameter"""

    def test_blank(self, model):
        """Test blank parameter for fields"""

        for instance in model.objects.all():
            for field in self.blank_fields:
                real_blank = instance._meta.get_field(field).blank

                self.assertTrue(real_blank)


class TestDefaultMixin:
    """Mixin with function for testing default parameter"""

    def test_default(self, model):
        """Test default parameter for fields"""

        test_parameter_of_field(
            model, self, self.field_and_default, 'default'
        )


class TestModelOrdering:
    """Mixin with function for testing ordering of model"""

    def test_ordering_of_model(self, model):
        """Test ordering of the model"""

        real_ordering = model._meta.ordering
        expected_ordering = self.model_ordering

        self.assertEqual(real_ordering, expected_ordering)


class TestModelVerboseNameMixin:
    """Mixin with function for testing verbose_name of model"""

    def test_verbose_name_of_model(self, model):
        """Test verbose_name of the model"""

        real_verbose_name = model._meta.verbose_name
        expected_verbose_name = self.model_verbose_name

        self.assertEqual(real_verbose_name, expected_verbose_name)


class TestModelVerboseNamePluralMixin:
    """Mixin with function for testing verbose_name_plural of model"""

    def test_verbose_name_plural_of_model(self, model):
        """Test verbose_name_plural of the model"""

        real_verbose_name_plural = model._meta.verbose_name_plural
        expected_verbose_name_plural = self.model_verbose_name_plural

        self.assertEqual(
            real_verbose_name_plural, expected_verbose_name_plural
        )


class TestObjectStringDisplayMixin:
    """Mixin with function for testing instance string display"""

    def test_object_string_display(self, object_, expected_string_display):
        """Test string display of the model instance"""

        real_string_display = str(object_)

        self.assertEqual(real_string_display, expected_string_display)


class TestModelUniqueTogether:
    """Mixin with function for testing unique_together of model"""

    def test_unique_together_of_model(self, model):
        """Test unique_together of the model"""

        real_unique_together = model._meta.unique_together
        expected_unique_together = self.model_unique_together

        self.assertEqual(*real_unique_together, expected_unique_together)


COMMON_MIXINS = (
    TestVerboseNameMixin, TestObjectStringDisplayMixin,
    TestModelVerboseNameMixin, TestModelVerboseNamePluralMixin,
)
