from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
import pytest

@pytest.mark.django_db
def test_user_exist_unsuccessful():
	# User.objects.get(id=1)
	with pytest.raises(ObjectDoesNotExist):
		User.objects.get(id=1)
