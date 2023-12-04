export function scrollToTarget(targetId) {
    var scrollTarget = document.getElementById(targetId);
    if (scrollTarget) {
        window.scrollTo({
            top: scrollTarget.offsetTop,
            behavior: 'smooth'
        });
    }
}
