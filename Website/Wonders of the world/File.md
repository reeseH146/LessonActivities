# Creating a website with the theme "Seven New Wonders of the World"
## Wonders : 
 - Pyramid of Giza - Not but PowerPoint says so
 - Great Wall of China
 - Petra
 - The Colosseum
 - Chichén Itza
 - Machu Picchu
 - Taj Mahal
 - Christ the Redeemer

## Requirements
 - Hyperlinks to other pages
 - Headings
 - Descriptions
 - Image
 - Bullet point of key facts
 - Form : 
    - First name
    - Second name
    - Email
    - Date of visit
    - Descriptions of experiences/memories/stuff

    - Alerts user if form incomplete under red of what is missing
    - Concatenates names and outputs 
    - Validates : 
       - Date - >=today's date and within proper ranges (Don't forget leap year)
       - Email - At least contains 1 "." and only 1 @ symbol

## Review
 - Since this was written in notepad with a weird font, some of the indents wrong
 - JS uses camelCase and I use PascalCase and keep switching between them which can cause confusion with variables/id/class/etc (camelCase for CSS due to element selectors being undercase)
 - Use of inline css combined with external, can be hard to debug rather than using id in place of inline
 - Could not figure out how to use CSS for these : 
    - Format the articles so that the textbox and imgage&table box are equal height
    - Make it mobile device friendly
    - Make the textarea in form page to resize based on available space (flexgrow or grid layout or @media queries)
    - Make text area and rest of form to rotate so that they don't squeeze in smaller width devices like mobile