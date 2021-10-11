from django.test import TestCase

# Create your tests here.
  <div class="dropdown-menu" aria-labelledby="navbarDropdown">
          <a class="dropdown-item" href="{% url 'newentry'%}">Add Entry</a>
          <a class="dropdown-item" href="#">Edit Entry</a>
          <a class="dropdown-item" href="{%url 'viewentry'%}"> View Entries</a>
          <a class="dropdown-item" href="#">Delete Entry</a>
          <div class="dropdown-divider"></div>
          <a class="dropdown-item" href="#">Something else here</a>
        </div>
     </li>
