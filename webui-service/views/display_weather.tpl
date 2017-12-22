% rebase('base.tpl')
<div class="container">
 <div class="row">
   <h1>{{header}}</h1>

   <div class="bs-example" data-example-id="hoverable-table"> 
     <table class="table table-hover"> 
       <thead> 
        <tr> 
          <th>Day</th> 
          <th>Description</th>
          <th>High</th>
          <th>Low</th>
          <th>Sunset</th> 
        </tr> 
       </thead> 
       <tbody>
         % for day in days:
          <tr> 
            <th scope="row">{{day[0]}}</th> <td>{{day[1]}}</td> <td>{{day[2]}}</td> <td>{{day[3]}}</td> <td>{{day[4]}}</td>
          </tr>
         % end 
       </tbody> 
      </table>
    </div>
   <div class="col-lg-6 col-md-6 col-sm-6 col-lg-offset-3 col-md-offset-3 col-sm-offset-3">
   <form action="/weather" method="post">
     <div class="form-group">
        <input id="address" class="form-control" name="address" type="text" placeholder="City, zip, or place" required>
     </div>
       <input class="btn btn-default btn-block" value="Get Weather" type="submit" />
   </form>
  </div>
 </div>
</div>
