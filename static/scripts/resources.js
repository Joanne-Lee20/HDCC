const ALL_RESRCS = document.getElementsByTagName("main")[0].getElementsByTagName("section");

let applyFilters = () => {
  let shouldShow = [];
  for (let i = 0; i < ALL_RESRCS.length; i++) {
    shouldShow.push(false);
  }

  parseFilter("media-types", 3, "<b>Platform/media type:</b> ".length, shouldShow);
  parseFilter("topics", 4, "<b>Topic:</b> ".length, shouldShow);

  for (let i = 0; i < ALL_RESRCS.length; i++) {
    ALL_RESRCS[i].style.display = shouldShow[i] ? "grid" : "none";
  }
}

/**
 * @param {string} filterSection    html element id for a certain filter section
 *                                  ex) the id of the media type section is "media-types"
 * 
 * @param {number} fieldIndex       corresponds to which field within the resource data the filter applies to;
 *                                  every resource has the fields title, author(s), description, media type, and topic
 *                                  ex) media type is the 4th field so the index is 3
 * 
 * @param {number} valueIndex       where to start substringing the innerHTML code to get the actual value of a field
 *                                  ex) for media type, since the innerHTML code is "<b>Platform/media type:</b> ...",
 *                                      the actual value of starts at index 28 (use string length, don't try to count)
 * 
 * @param {Array} shouldShow        boolean occurrency array for whether to show a resource or not
 */
let parseFilter = (filterSection, fieldIndex, valueIndex, shouldShow) => {
  let filters = [];
  let checkboxes = document.getElementById(filterSection).getElementsByTagName("input");

  for (let checkbox of checkboxes) {
    if (checkbox.checked) {
      filters.push(checkbox.value);
    }
  }

  for (let i = 0; i < ALL_RESRCS.length; i++) {
    let field = ALL_RESRCS[i].children[1].children[fieldIndex];
    let value = field.innerHTML.substring(valueIndex);
    if (filters.includes(value)) {
      shouldShow[i] = true;
    }
  }
}