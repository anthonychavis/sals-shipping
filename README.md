# Sal's Shipping

Practicing control flow & file handling with Python 3

## Table of Contents

- [Introduction](#introduction)
  - [Shipping Cost](#shipping-cost)
- [Technologies](#technologies)
- [Sources](#sources)
- [Extra Info](#extra-info)
- [Contact Me](#contact)
  <!-- - [Launch](#launch) -->
  <!-- - [Design System](#design-system) -->
    <!-- -   [Flowchart](#flowchart) -->
    <!-- -   [Architectrure](#architecture) -->

## Introduction

Sal has a shipping company and wants to help her customers find the lowest-cost method of shipping their packages. So, it's my job to write the program to help her customers decide between 3 shipping methods:

1. drone shipping
2. ground shipping,
3. premium ground shipping

### Shipping Cost

#### Drone Shipping

| Package Weight (lbs)                  | Price / Pound ($ / lb) | Flat Fee ($) |
| :------------------------------------ | :--------------------: | :----------: |
| less than or equal to 2               |          4.50          |     0.00     |
| more than 2, less than or equal to 6  |          9.00          |     0.00     |
| more than 6, less than or equal to 10 |         12.00          |     0.00     |
| more than 10                          |         14.25          |     0.00     |

#### Ground Shipping

| Package Weight (lbs)                  | Price / Pound ($ / lb) | Flat Fee ($) |
| :------------------------------------ | :--------------------: | :----------: |
| less than or equal to 2               |          1.50          |    20.00     |
| more than 2, less than or equal to 6  |          3.00          |    20.00     |
| more than 6, less than or equal to 10 |          4.00          |    20.00     |
| more than 10                          |          4.75          |    20.00     |

#### **Premium Ground Shipping** = $125.00

## Technologies

- Python 3
- VSCode

<!-- ## Launch

[Live site][live-site] -->

<!-- ## Design System

Cheat Sheet's [design system][design-system] -->

<!-- ## Flowchart

 ![Flowchart][flowchart] -->

<!-- ## Architecture

 ![Architecture][architecture] -->

## Sources

The inspiration for this project was Codecademy's Python 3: Control Flow project called [Sal's Shipping][lesson-site].

They provided [example code][example-site] of how to complete the job.

## Extra Info

A lot is different from Codecademy's practice project.

- About the README:
  - The [Shipping Cost](#shipping-cost) content was added to this README file programmatically
    - _because why would I type tables out in 5 minutes when I could spend much, much more time figuring out how to write a [file-handling program][file-handle-program] to add the tables for me?_
  - Need to look into the error handling for the file-handling program
- About the [program to help Sal & her customers][find-low-shipping-program]:
  - It is currently set to print the results to the terminal
    - _it'll likely remain that way for a long time since I'd rather spend more time with Big O at the moment_
  - Challenged myself to try syntax that's newer to me
    - _there are likely parts of the program that you'd wish were more readable_
    - _in a few months from now, I'll probably wish the same_
  - It is simplified to a function that will take the package weight as an argument
    - _could've written the return/print message a bit differently to better present the info to the customer_
  - There are example function calls in the [use_the_fxn][use-fxn] file
    - _the purpose of this file is to practice importing functions in Python_
  - Need to verify the function's argument type
    - _verify/sanitize user input_
- Critique:
  - I'm open to criticism; very much want to improve rapidly
  - If you notice something weird, or unsafe, or have food for thought, please don't hesitate to let me know

## Contact

[Anthony Chavis][email]

### Return to the [Table of Contents](#table-of-contents)

### Return to the [top](#)

<!-- [live-site]: -->
<!-- [design-system]:  -->

<!-- [flowchart]:  -->
<!-- [architecture]:  -->

[file-handle-program]: https://github.com/anthonychavis/sals-shipping/blob/main/readme_table_gen.py
[use-fxn]: https://github.com/anthonychavis/sals-shipping/blob/main/use_the_fxn.py
[find-low-shipping-program]: https://github.com/anthonychavis/sals-shipping/blob/main/low_shipping.py
[lesson-site]: https://www.codecademy.com/courses/learn-python-3/projects/python-sals-shipping
[example-site]: https://github.com/Codecademy/learn-python/blob/main/2-control-flow/sals-shipping/shipping.py
[email]: gitanthony@yahoo.com
