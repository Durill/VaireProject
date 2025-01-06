__all__ = ('IWeaver',)

from abc import ABC, abstractmethod


class IWeaver(ABC):
    @abstractmethod
    def _rgb_mode(self):
        raise NotImplementedError
