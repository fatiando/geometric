{{ fullname | escape | underline }}

.. currentmodule:: {{ module }}

.. autoclass:: {{ objname }}

    {% block methods_documentation %}
    {% if methods %}

    .. rubric:: Methods Documentation

    {% for item in methods %}
    {% if item != '__init__' %}
    .. automethod:: {{ item }}
    {% endif %}
    {% endfor %}

    {% endif %}
    {% endblock %}

.. include:: ../backreferences/{{ fullname }}.examples

.. raw:: html

     <div style='clear:both'></div>

