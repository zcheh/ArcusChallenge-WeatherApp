% rebase('base.tpl')
<h1>{{header}}</h1>
<ul>
 % for day in days:
    <li>{{day}}</li>
 % end
</ul>
<form action="/weather" method="post">
    Latitude: <input name="lat" type="text" />
    Longitude: <input name="long" type="text" />
    <input value="Get Weather" type="submit" />
</form>
