# Battery and Regulators

## Battery 
<img style="width:40%; margin:0 50px 0 50px; float:left;" src="https://sc04.alicdn.com/kf/H679bc52188464178b6d691d1a91de5cfP.jpg"/>
<img style="width:40%;" src="http://sc04.alicdn.com/kf/H0fd0f1acec0342899e9b45ce4fa5bbdeT.jpg"/>

The power required for the operation of all systems on Cloudy is obtained from 18650 lion batteries in a 6s1p arrangement.The 3200mAh capacity of the battery allows Cloudy to run for a duration of over two hour. By modifying the battery cover to accommodate larger batteries, the operating time can potentially be extended to 10 hours.

| Payload 	| Test Type 	| Duration 	| BattV Starting 	| BattV Finishing 	| Notes 	|
|:---:	|:---:	|:---:	|:---:	|:---:	|:---:	|
| 2KG 	| Driving 	| 30 Minutes 	| 24.2 	| 22.9 	| Ok 	|
| 8KG 	| Driving 	| 30 Minutes 	| 22.9 	| 21.95 	| Ok 	|
| 0KG 	| Stopping 	| 30 Minutes 	| 21.95 	| 21.48 	| Ok 	|

## Voltage Regulators

<img style="width:40%; margin:0 50px 0 50px; float:left;" src="https://cdn.shopify.com/s/files/1/1840/1085/products/HWUBEC1.jpg?v=1603048312"/>
<img style="width:40%;" src="https://st3.myideasoft.com/idea/bx/32/myassets/products/549/henge-8a-ubec-regulator-rc-ubec.jpg?revision=1541522707"/>

Battery Eliminator Circuit (BEC) is converting battery voltage to demanded voltage such as 5V. Cloudy robot's SBC and microcontroller works with 5v. Since both can draw high currents, separate bec circuits are used in the robot for both. <a href="https://tr.aliexpress.com/item/32256292826.html?pdp_npi=2%40dis%21TRY%21TRY%20473.93%21TRY%20236.95%21%21%21%21%21%40211b446516777645114013824e2321%2112000028967443703%21btf&_t=pvid%3Aa7db28e0-30b3-408c-8964-39b7a42f84a8&afTraceInfo=32256292826__pc__pcBridgePPC__xxxxxx__1677764511&spm=a2g0o.ppclist.product.mainProduct&gatewayAdapt=glo2tur">Hobbywing 5V 3A</a> bec circuit can give 15w, is enought for microcontroller and Raspberry Pi 4. But if you want more power <a href="https://tr.aliexpress.com/item/4000013753385.html?pdp_npi=2%40dis%21TRY%21TRY%20160.18%21TRY%20160.17%21%21%21%21%21%40211b446516777646754255619e2321%2110000000034287844%21btf&_t=pvid%3A8b55dd82-d8d1-47b4-83b8-5c99c8c8bf95&afTraceInfo=4000013753385__pc__pcBridgePPC__xxxxxx__1677764675&spm=a2g0o.ppclist.product.mainProduct&gatewayAdapt=glo2tur">Henge 5V 6A </a>bec circuit is a good choice.
