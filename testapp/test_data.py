data_sources = [
{
  "icon": "customer",
  "table_id": "0",
  "table_name": "Customers",
  "meta":{
    "distribution": [
      1,
      3,
      3,
      5,
      2,
      8,
      10,
      4
    ],
    "labels":["AT&T","CISCO","NOKIA","BT","MSFT","IBM","FB","3M"],
    "entity_name": "Customer",
    "taxonomy": "Existing and active end customer unique identifier that represents",
    "owner": "prinkan.pal@legoai.com",
    "source": "SFDC/CUST_DIM/ONTO/RE",
    "data_type": [
      "string",
      "label"
    ],
    "dq_score": "high",
    "importance": "high"
  }
},
{
  "icon": "customer_sales",
  "table_id": "1",
  "table_name": "Customer_Sales"
},
{
    "icon": "products",
    "table_id": "2",
    "table_name": "Products",
},
{
    "icon": "sellers",
    "table_id": "3",
    "table_name": "Sellers"
},
{
    "icon": "orders",
    "table_id": "4",
    "table_name": "Orders"
},
{
    "icon": "orders_payments",
    "table_id": "6",
    "table_name": "Order Payments"
},
{
    "icon": "orders_reviews",
    "table_id": "7",
    "table_name": "Order Reviews"
},
{
    "icon": "orders_items",
    "table_id": "8",
    "table_name": "Order Items"
}
]   

metadata_customers = {
  "distribution": [
  1,
  3,
  3,
  5,
  2,
  8,
  10,
  4
  ],
  "labels":["AT&T","CISCO","NOKIA","BT","MSFT","IBM","FB","3M"],
  "entity_name": "Customer",
  "taxonomy": "Existing and active end customer unique identifier that represents",
  "owner": "prinkan.pal@legoai.com",
  "source": "SFDC/CUST_DIM/ONTO/RE",
  "data_type": [
  "string",
  "label"
  ],
  "dq_score": "high",
  "importance": "high"
}


metadata_customers_cols = {
  "Cust_ID": {
    "distribution": [
      1,
      3,
      3,
      5,
      2,
      8,
      10,
      4
    ],
    "entity_name": "Customer",
    "taxonomy": "Existing and active end customer unique identifier that represents",
    "owner": "prinkan.pal@legoai.com ",
    "source": "SFDC/CUST_DIM/ONTO/RE",
    "data_type": [
      "string",
      "label"
    ],
    "dq_score": "high",
    "importance": "high"
  },
  "Customer_ID": {
    "distribution": [
      1,
      3,
      3,
      5,
      2,
      8,
      10,
      4
    ],
    "entity_name": "Customer",
    "taxonomy": "Existing and active end customer unique identifier that represents",
    "owner": "prinkan.pal@legoai.com ",
    "source": "SFDC/CUST_DIM/ONTO/RE",
    "data_type": [
      "string",
      "label"
    ],
    "dq_score": "high",
    "importance": "high"
  },
  "Cust_Name": {
    "distribution": [
      1,
      3,
      3,
      5,
      2,
      8,
      10,
      4
    ],
    "entity_name": "Customer",
    "taxonomy": "Existing and active end customer unique identifier that represents",
    "owner": "prinkan.pal@legoai.com ",
    "source": "SFDC/CUST_DIM/ONTO/RE",
    "data_type": [
      "string",
      "label"
    ],
    "dq_score": "high",
    "importance": "high"
  },
  "Geo_Region": {
    "distribution": [
      1,
      3,
      3,
      5,
      2,
      8,
      10,
      4
    ],
    "entity_name": "Customer",
    "taxonomy": "Existing and active end customer unique identifier that represents",
    "owner": "prinkan.pal@legoai.com ",
    "source": "SFDC/CUST_DIM/ONTO/RE",
    "data_type": [
      "string",
      "label"
    ],
    "dq_score": "high",
    "importance": "high"
  },
  "Geo_Country": {
    "distribution": [
      1,
      3,
      3,
      5,
      2,
      8,
      10,
      4
    ],
    "entity_name": "Customer",
    "taxonomy": "Existing and active end customer unique identifier that represents",
    "owner": "prinkan.pal@legoai.com ",
    "source": "SFDC/CUST_DIM/ONTO/RE",
    "data_type": [
      "string",
      "label"
    ],
    "dq_score": "high",
    "importance": "high"
  },
  "Prod_Name": {
    "distribution": [
      1,
      3,
      3,
      5,
      2,
      8,
      10,
      4
    ],
    "entity_name": "Customer",
    "taxonomy": "Existing and active end customer unique identifier that represents",
    "owner": "prinkan.pal@legoai.com ",
    "source": "SFDC/CUST_DIM/ONTO/RE",
    "data_type": [
      "string",
      "label"
    ],
    "dq_score": "high",
    "importance": "high"
  },
  "Revenue": {
    "distribution": [
      1,
      3,
      3,
      5,
      2,
      8,
      10,
      4
    ],
    "entity_name": "Customer",
    "taxonomy": "big text",
    "owner": "ljkj",
    "source": "rtyu",
    "data_type": [
      "string",
      "label"
    ],
    "dq_score": "low",
    "importance": "df"
  },
  "NAICS_Code": {
    "distribution": [
      1,
      3,
      3,
      5,
      2,
      8,
      10,
      4
    ],
    "entity_name": "Customer",
    "taxonomy": "big text",
    "owner": "",
    "source": "",
    "data_type": [
      "string",
      "label"
    ],
    "dq_score": "",
    "importance": ""
  },
  "NAICS_Industry": {
    "distribution": [
      1,
      3,
      3,
      5,
      2,
      8,
      10,
      4
    ],
    "entity_name": "Customer",
    "taxonomy": "big text",
    "owner": "",
    "source": "",
    "data_type": [
      "string",
      "label"
    ],
    "dq_score": "",
    "importance": ""
  },
  "Cust_Status": {
    "distribution": [
      1,
      3,
      3,
      5,
      2,
      8,
      10,
      4
    ],
    "entity_name": "Customer",
    "taxonomy": "big text",
    "owner": "",
    "source": "",
    "data_type": [
      "string",
      "label"
    ],
    "dq_score": "",
    "importance": ""
  }
}


Gov_Transformations_data = [
  [
    "Recipe ID",
    "Type",
    "Execution Status",
    "Spark Query",
    "Domain",
    "Nodes",
    "Function",
    "Details",
  ],
  [
    "TR_4848",
    "https://legoai.com/assets/ontocraft/settingSecondary.png",
    "https://legoai.com/assets/ontocraft/success.png",
    "https://legoai.com/assets/ontocraft/eye.png",
    "CUSTOMER",
    "Cust ID, Party Name",
    "CONCATE",
    "......",
  ],
  [
    "DQ_8474",
    "https://legoai.com/assets/ontocraft/badge.png",
    "https://legoai.com/assets/ontocraft/success.png",
    "https://legoai.com/assets/ontocraft/eye.png",
    "PRODUCT",
    "Product_ID",
    "IS NULL",
    "......",
  ],
  [
    "TR_8363",
    "https://legoai.com/assets/ontocraft/settingSecondary.png",
    "https://legoai.com/assets/ontocraft/success.png",
    "https://legoai.com/assets/ontocraft/eye.png",
    "SUPPLYCHAIN",
    "Ship_Date",
    "TO DATE",
    "......",
  ],
  [
    "LK_294",
    "https://legoai.com/assets/ontocraft/intersection.png",
    "https://legoai.com/assets/ontocraft/success.png",
    "https://legoai.com/assets/ontocraft/eye.png",
    "CUSTOMER,SUPPORT",
    "Cust_ID,C_ID",
    "ISNULL, INNERJOIN",
    "......",
  ],
  ["TR_8374", "https://legoai.com/assets/ontocraft/settingSecondary.png", "https://legoai.com/assets/ontocraft/failure.png", "https://legoai.com/assets/ontocraft/eye.png", "MARKETING", "Interaction_ID", "COUNTD", "......"],
  [
    "LK_7384",
    "https://legoai.com/assets/ontocraft/intersection.png",
    "https://legoai.com/assets/ontocraft/success.png",
    "https://legoai.com/assets/ontocraft/eye.png",
    "PRODUCT,MARKETING",
    "Product_ID,Prod_ID",
    "INNERJOIN",
    "......",
  ],
  [
    "TR_3758",
    "https://legoai.com/assets/ontocraft/settingSecondary.png",
    "https://legoai.com/assets/ontocraft/success.png",
    "https://legoai.com/assets/ontocraft/eye.png",
    "SUPPLY CHAIN",
    "Inv_ID",
    "COUNT",
    "......",
  ],
  [
    "TR_7645",
    "https://legoai.com/assets/ontocraft/settingSecondary.png",
    "https://legoai.com/assets/ontocraft/failure.png",
    "https://legoai.com/assets/ontocraft/eye.png",
    "SUPPLY CHAIN",
    "Inv_ID",
    "COUNT",
    "......",
  ],
  [
    "LK_9365",
    "https://legoai.com/assets/ontocraft/intersection.png",
    "https://legoai.com/assets/ontocraft/failure.png",
    "https://legoai.com/assets/ontocraft/eye.png",
    "SUPPLY CHAIN, SUPPORT",
    "Odr_ID, Return_ID",
    "INNERJOIN",
    "......",
  ],
  ["TR_138", "https://legoai.com/assets/ontocraft/settingSecondary.png", "https://legoai.com/assets/ontocraft/minusSolid.png", "https://legoai.com/assets/ontocraft/eye.png", "MARKETING", "Click_ID, Prospect_ID", "ORDERBY", "......"],
  [
    "TR_3957",
    "https://legoai.com/assets/ontocraft/settingSecondary.png",
    "https://legoai.com/assets/ontocraft/failure.png",
    "https://legoai.com/assets/ontocraft/eye.png",
    "PRODUCT, SUPPORT",
    "Product_ID, Prod_ID",
    "OUTERJOIN",
    "......",
  ],
  ["TR_823", "https://legoai.com/assets/ontocraft/settingSecondary.png", "https://legoai.com/assets/ontocraft/minusSolid.png", "https://legoai.com/assets/ontocraft/eye.png", "SUPPORT", "SR_ID", "UNIQUE", "......"],
  [
    "TR_923",
    "https://legoai.com/assets/ontocraft/settingSecondary.png",
    "https://legoai.com/assets/ontocraft/minusSolid.png",
    "https://legoai.com/assets/ontocraft/eye.png",
    "CUSTOMER, MARKETING",
    "Cust_ID, Prospect_ID",
    "INNERJOIN",
    "......",
  ],
  ["DQ_385", "https://legoai.com/assets/ontocraft/badge.png", "https://legoai.com/assets/ontocraft/minusSolid.png", "https://legoai.com/assets/ontocraft/eye.png", "PRODUCT", "Prod_Desc", "TRIM", "......"],
  [
    "LK_3947",
    "https://legoai.com/assets/ontocraft/intersection.png",
    "https://legoai.com/assets/ontocraft/success.png",
    "https://legoai.com/assets/ontocraft/eye.png",
    "SUPPLY CHAIN, SUPPORT",
    "Odr_ID, Return_ID",
    "INNERJOIN",
    "......",
  ],
  [
    "TR_923",
    "https://legoai.com/assets/ontocraft/settingSecondary.png",
    "https://legoai.com/assets/ontocraft/minusSolid.png",
    "https://legoai.com/assets/ontocraft/eye.png",
    "CUSTOMER, MARKETING",
    "Cust_ID, Prospect_ID",
    "INNERJOIN",
    "......",
  ],
  [
    "TR_923",
    "https://legoai.com/assets/ontocraft/settingSecondary.png",
    "https://legoai.com/assets/ontocraft/minusSolid.png",
    "https://legoai.com/assets/ontocraft/eye.png",
    "CUSTOMER, MARKETING",
    "Cust_ID, Prospect_ID",
    "INNERJOIN",
    "......",
  ],
  [
    "TR_923",
    "https://legoai.com/assets/ontocraft/settingSecondary.png",
    "https://legoai.com/assets/ontocraft/minusSolid.png",
    "https://legoai.com/assets/ontocraft/eye.png",
    "CUSTOMER, MARKETING",
    "Cust_ID, Prospect_ID",
    "INNERJOIN",
    "......",
  ],
  [
    "TR_923",
    "https://legoai.com/assets/ontocraft/settingSecondary.png",
    "https://legoai.com/assets/ontocraft/minusSolid.png",
    "https://legoai.com/assets/ontocraft/eye.png",
    "CUSTOMER, MARKETING",
    "Cust_ID, Prospect_ID",
    "INNERJOIN",
    "......",
  ],
  [
    "TR_923",
    "https://legoai.com/assets/ontocraft/settingSecondary.png",
    "https://legoai.com/assets/ontocraft/minusSolid.png",
    "https://legoai.com/assets/ontocraft/eye.png",
    "CUSTOMER, MARKETING",
    "Cust_ID, Prospect_ID",
    "INNERJOIN",
    "......",
  ]
]


gov_access_data = [
    # ["Group/User", "Role", "eyeHollowIcon", "noteIcon", "compassIcon", "filterIcon", "cartIcon", "downloadIcon", "settingGreyIcon", "ribbonGreyIcon", "unionGreyIcon", "tuneIcon", "lockGreyIcon", "uploadGreyIcon", "binIcon"],
    ["All Users", "Viewer", "Y", "N", "Y", "N", "N", "Y", "N", "N", "N", "Y", "N", "N", "N"],
    ["Group", "Explorer", "Y", "O", "O", "O", "Y", "Y", "O", "O", "O", "Y", "N", "N", "N"],
    ["John", "Admin", "Y", "Y", "Y", "Y", "Y", "Y", "Y", "Y", "Y", "Y", "Y", "Y", "Y"],
    ["Marie", "Publisher", "Y", "Y", "Y", "Y", "Y", "Y", "O", "O", "O", "Y", "Y", "Y", "N"],
    ["Laura", "Modeler", "Y", "Y", "Y", "Y", "Y", "Y", "Y", "Y", "Y", "Y", "Y", "Y", "N"],
    ["Will", "Consumer", "Y", "N", "N", "N", "Y", "Y", "O", "O", "O", "Y", "Y", "Y", "N"],
    ["Harris", "Custom", "Y", "N", "N", "Y", "Y", "Y", "O", "O", "O", "Y", "N", "N", "N"],
    ["Daniel", "Custom", "Y", "N", "N", "Y", "O", "O", "O", "O", "O", "Y", "N", "N", "N"],
    ["Jenny", "Custom", "Y", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
  ]