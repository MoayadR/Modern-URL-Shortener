function visits(element)
{
    window.open(element.value , '_blank');
}
function copy(element)
{
    navigator.clipboard.writeText(element.value);
}

function deleteURL(element)
{
    let statusBool = window.confirm("Are your sure you want to delete this URL?");
    if (statusBool)
    {
        window.open("http://127.0.0.1:8000/url/delete/" +element.value);
    }

}