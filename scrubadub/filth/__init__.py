import os
import re

from ..import_magic import iter_subclasses, update_locals
from .base import Filth, MergedFilth
from .address import AddressFilth
from .credential import CredentialFilth
from .email import EmailFilth
from .known import KnownFilth
from .name import NameFilth
from .organization import OrganizationFilth
from .phone import PhoneFilth
from .skype import SkypeFilth
from .ssn import SSNFilth
from .url import UrlFilth


def _is_abstract_filth(filth_cls):
    """Filth must have a ``type`` defined"""
    return filth_cls.type is None


def iter_filth_clss():
    """Iterate over all of the filths that are included in this sub-package.
    This is a convenience method for capturing all new Filth that are added
    over time.
    """
    return iter_subclasses(
        os.path.dirname(os.path.abspath(__file__)),
        Filth,
        _is_abstract_filth,
    )


def iter_filths():
    """Iterate over all instances of filth"""
    for filth_cls in iter_filth_clss():
        yield filth_cls()


# import all of the detector classes into the local namespace to make it easy
# to do things like `import scrubadub.detectors.NameDetector`
# update_locals(locals(), iter_filths)
