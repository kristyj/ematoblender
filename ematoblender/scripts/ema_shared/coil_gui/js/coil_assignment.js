console.log("script working");

var x = 10;
var current_filled = [];
var cellval;

function refresh_todo_list(){
	console.log(current_filled);
	//console.log(x);

	var todolist = document.getElementById("alloc-status");
	var child = todolist.firstChild;

	while(child) {
		console.log(child, child.tagName);
			if (current_filled.indexOf(""+child.innerHTML) >= 0){
				console.log('hiding');
				try{
					child.style.opacity = 0.2;
				} catch(err){
					console.log(err.message);
				}
			}
			else{
				try{
					child.style.opacity = 1.0;
				}catch(err){
					console.log(err.message);
				}
			}
		
    	child = child.nextSibling;
	}
}
 

// on adding an input, change the list
function push_index_input(cell){
	cellval = "" + cell.value;
	current_filled.push(cellval);
	console.log(current_filled);
	//current_filled.push('a');
	//x ++;
}

// on removing an input, change the list
function pop_index_input(cell){
	var oldval = "" + cell.value;
	place = current_filled.indexOf(oldval);
	if (place >= 0){
		current_filled = delete_at_index(current_filled, place);
	}
}

// delete something at a list's index
function delete_at_index(list, ind){
	return list.slice(0, ind).concat(list.slice(ind+1));
}

