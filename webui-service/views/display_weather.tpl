% rebase('base.tpl')
<h1>{{header}}</h1>
<ul>
 % for day in days:
    <li>{{day}}</li>
 % end
</ul>
<form action="/weather" method="post">
    City, State or Country: <input name="address" type="text" />
    <input value="Get Weather" type="submit" />
</form>
