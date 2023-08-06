function visits(element)
{
    window.open(element.value , '_blank');
}
function copy(element)
{
    navigator.clipboard.writeText(element.value);
}