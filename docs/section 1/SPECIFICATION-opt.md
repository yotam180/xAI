# Specification Document

## 1. _Purpose_ ##


The goal of this project is to provide an API for programmers to easily classify and process the contents of images, and by that to demonstrate the capabilites and concepts of Supervised Learning in the field of Machine Leraning.

## 2. _Scope_ ##

The "xAI Vision" is an API, publically available in various interfaces, which's purpose is to recognize images' contents and to classify them, in a simple way for new programmers to integrate with and for novice researchers in the field of AI to get along with neural network design concepts via the open source nature of the project.

## 3. _Product Perspective_ ##

The REST API would have to communicate over Internet Network.

### 3.1 _System Interfaces_ ###

1. Microsoft's **httpd** for HTTP server (REST API server)
2. Possible - GPU card for network training acceleration.

### 3.2 _User Interfaces_ ###

> A newcoming user will enter the GUI version of the software, will see 3 options - extending categories, creating categories, and classifying images. No login would be required for the demo GUI version.
> 
> Selecting the 'create category' button would lead to a different form. The user will be asked to enter iamge URLs or select local storage images that apply for the category. The user will also be asked if they wish to create the category locally on their computer, or train the global network on the xAI vision servers. After submission, they will be asked to verify that a list of random images they will be given is **not** of the same categoy they have just created. They will be able to verify or mark the image as correct, and they will be applied to the same category. The user will be asked if they wish to enter specific images that do not classify to their newly created category. After the progress is done, they are redirected to the main screen.
> 
> Clicking the 'extend category' will show an alphabetically ordered list of all registered classes. After choosing a class to extend, they will be able to upload images and select if they classify to the category or not.
> 
> Clicking the 'classify image' will show a form, asking the user to enter an image. After entring an image the user will be shown the results of the network feed-forward (what the image was classified as) and will be given some similar images from the same category.

[ optional - entering images]

### 3.3 _Hardware Interfaces_ ###

The system has no hardware interfaces.

### 3.4 _Software Interfaces_ ###

#### C++ NeuronLib interface ####
An own-made interface for mathematical operations and for neural networks, providing a fast way to perform mathematical calculations and to design convolutional neural networks. 
 
The interface mainly defines the `Mat` (matrix) and `Vec` (vector) classes, and multiple and various math operations like `dot`, `cross`, `+ - * /`, masking operations and different utilities to work with mathematical objects. 

All source code for the library is included and self-made (no 3rd party software).

### 3.5 _Communication Interfaces_ ###

Specify the various interfaces to communications such as local network protocols.

### 3.6 _Memory Constraints_ ###

Specify any applicable characteristics and limits on primary and secondary memory.

### 3.7 _Operations_ ###

Specify the normal and special operations required by the user such as:

+ The various modes of operations in the user organization (e.g., user-initiated operations);
+ Periods of interactive operations and periods of unattended operations;
+ Data processing support functions;
+ Backup and recovery operations.

This is sometimes specified as part of the User Interfaces section.

### 3.8 _Site Adaptations_ ###

The site adaptation requirements include:

+ Definition of the requirements for any data or initialization sequences that are specific to a given site, mission, or operational mode (e.g., grid values, safety limits, etc.);
+ Specification of the site or mission-related features that should be modified to adapt the software to a particular installation.

## 4. _Product Functions_ ##

Provide a summary of the major functions that the software will perform. For example, an SRS for an accounting program may use this part to address customer account maintenance, customer statement, and invoice preparation without mentioning the vast amount of detail that each of those functions requires.

Sometimes the function summary that is necessary for this part can be taken directly from the section of the higher-level specification (if one exists) that allocates particular functions to the software product.

Note that for the sake of clarity:

+ The product functions should be organized in a way that makes the list of functions understandable to the acquirer or to anyone else reading the document for the first time;
+ Textual or graphical methods can be used to show the different functions and their relationships. Such a diagram is not intended to show a design of a product, but simply shows the logical relationships among variables.

## 5. _User Characteristics_ ##

Describe those general characteristics of the intended groups of users of the product including characteristics that may influence usability, such as educational level, experience, disabilities, and technical expertise. This description should not state specific requirements, but rather should state the reasons why certain specific requirements are later specified in specific requirements. Where appropriate, the user characteristics of the SyRS and SRS should be consistent.

## 6. _Limitations_ ##

Provide a general description of any other items that will limit the supplier's options, including:

+ Regulatory policies;
+ Hardware limitations (e.g., signal timing requirements);
+ Interfaces to other applications;
+ Parallel operation;
+ Audit functions;
+ Control functions;
+ Higher-order language requirements;
+ Signal handshake protocols (e.g., XON-XOFF, ACK-NACK);
+ Quality requirements (e.g., reliability);
+ Criticality of the application;
+ Safety and security considerations;
+ Physical/mental considerations

## 7. _Assumptions and Dependencies_ ##

List each of the factors that affect the requirements stated in the SRS. These factors are not design constraints on the software but any changes to these factors can affect the requirements in the SRS. For example, an assumption may be that a specific operating system will be available on the hardware designated for the software product. If, in fact, the operating system is not available, the SRS would then have to change accordingly.

## 8. _Apportioning of Requirements_ ##

Apportion the software requirements to software elements. For requirements that will require implementation over multiple software elements, or when allocation to a software element is initially undefined, this should be so stated. A cross reference table by function and software element should be used to summarize the apportionments.

Identify requirements that may be delayed until future versions of the system (e.g., blocks and/or increments).

## 9. _Specific Requirements_ ##

Specify all of the software requirements to a level of detail sufficient to enable designers to design a software system to satisfy those requirements.

Specify all of the software requirements to a level of detail sufficient to enable testers to test that the software system satisfies those requirements.

At a minimum, describe every input (stimulus) into the software system, every output (response) from the software system, and all functions performed by the software system in response to an input or in support of an output.

The specific requirements should:

+ Be stated in conformance with all the characteristics described in 5.2 of this International Standard;
+ Be cross-referenced to earlier documents that relate;
+ Be uniquely identifiable.

## 10. _External Interfaces_ ##

Define all inputs into and outputs from the software system. The description should complement the interface descriptions in 3.1 through 3.5, and should not repeat information there.

Each interface defined should include the following content:

+ Name of item;
+ Description of purpose;
+ Source of input or destination of output;
+ Valid range, accuracy, and/or tolerance;
+ Units of measure;
+ Relationships to other inputs/outputs;
+ Screen formats/organization;
+ Window formats/organization;
+ Data formats;
+ Command formats;
+ End messages.

## 11. _Functions_ ##

Define the fundamental actions that have to take place in the software in accepting and processing the inputs and in processing and generating the outputs, including:

+ Validity checks on the inputs;
+ Exact sequence of operations;
+ Responses to abnormal situations, including Communication facilities and Error handling and recovery;
+ Effect of parameters;
+ Relationship of outputs to inputs, including Input/output sequences and Formulas for input to output conversion.

It may be appropriate to partition the functional requirements into subfunctions or subprocesses. This does not imply that the software design will also be partitioned that way.

> Partial example:
> 
> There are three types of users that interact with the system: users of the mobile application (User Class 1- User), restaurant owners (User Class 2 - Restaurant Owner) and administrators (User Class 3 - Administrator). Each of these three types of users has different use of the system so each of them has their own requirements.
> 
> **User Class 1 - User**
> 
> **Functional requirement 1.3**
> 
> ID: FR3
> 
> TITLE: User registration - Mobile application
> 
> DESC: After user has downloaded the mobile application, then he/she is able to register through the mobile application. The user must provide user-name, password and e-mail address. The user can choose to provide a regularly used phone number.
> 
> <hr/>
> 
> **Functional requirement 1.4**
> 
> ID: FR4
> 
> TITLE: User log-in - Mobile application
> 
> DESC: After user has registered, then he/she should be able to log in to the mobile application. The log-in information is stored on the phone and in future the user will be logged in automatically.
> 
> <hr/>
> 
> **Functional requirement 1.5**
> 
> ID: FR5
> 
> TITLE: Retrieve password
> 
> DESC: After user has registered, then he/she is able to retrieve his/her password by e-mail.
> 
> <hr/>
> 
> **User Class 3 - Administrator**
> 
> **Functional requirement 3.7**
> 
> ID: FR7
> 
> _Feature: Manage restaurant owners_
> 
> In order to keep track of the restaurant owners an administrator is able to manage the restaurant owners.
> 
> _Scenario: Add a new restaurant owner_
> 
> When the administrator creates a new restaurant owner<br/>
> Then the new restaurant owner should be added
> 
> _Scenario: Edit an existing restaurant owner_
> 
> When the administrator edits an existing restaurant owner<br/>
> Then the restaurant owner information should be updated
> 
> _Scenario: Delete an existing restaurant owner_
> 
> When the administrator deletes an existing restaurant owner<br/>
> Then the restaurant owner is deleted<br/>
> And the restaurant information is deleted

## 12. _Usability Requirements_ ##

Define usability (quality in use) requirements. Usability requirements and objectives for the software system include measurable effectiveness, efficiency, and satisfaction criteria in specific contexts of use.

## 13. _Performance Requirements_ ##

Specify both the static and the dynamic numerical requirements placed on the software or on human interaction with the software as a whole.

Static numerical requirements may include the following:

+ The number of terminals to be supported;
+ The number of simultaneous users to be supported;
+ Amount and type of information to be handled.
+ Static numerical requirements are sometimes identified under a separate section entitled Capacity.

Dynamic numerical requirements may include, for example, the numbers of transactions and tasks and the amount of data to be processed within certain time periods for both normal and peak workload conditions.

The performance requirements should be stated in measurable terms.

For example, «95 % of the transactions shall be processed in less than 1 second» rather than, «An operator shall not have to wait for the transaction to complete».

Numerical limits applied to one specific function are normally specified as part of the processing subparagraph description of that function.

> Partial example:
> 
> Quality requirement 6
> 
> ID: QR6
> 
> TITLE: The response time of a search.
> 
> DESCRIPTION: The response time of a search is the overall time beginning with the initial user action (click on the search button) on the mobile device, the request going to server, the response received from the server, and finally the response processing by the mobile application.
> 
> + METER: Measurements obtained from 1000 searches during testing (iOS 9, Android 5.0).<br/>
> + MUST: No more than 2 seconds during 100% of the searches during testing.<br/>
> + WISH: No more than 1 second during 100% of the searches during testing.<br/>

## 14. _Verification_ ##

Provide the verification approaches and methods planned to qualify the software. The information items for verification are recommended to be given in a parallel manner with the information items in subclause 10 to 17.

## 15. _Supporting Information_ ##

The SRS should contain additional supporting information including:

+ Sample input/output formats, descriptions of cost analysis studies, or results of user surveys;
+ Supporting or background information that can help the readers of the SRS;
+ A description of the problems to be solved by the software;
+ Special packaging instructions for the code and the media to meet security, export, initial loading, or other requirements.

The SRS should explicitly state whether or not these information items are to be considered part of the requirements.

> Partial example: Appendix 
