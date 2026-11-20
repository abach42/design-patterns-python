from designpatterns.structural.proxy.proxy import Proxy
from designpatterns.structural.proxy.real_subject import RealSubject


def test_proxy_delegates_to_real_subject() -> None:
    real = RealSubject()
    proxy = Proxy(real)

    result = proxy.get_data()

    assert result == "real Values"
    assert proxy.was_accessed()
