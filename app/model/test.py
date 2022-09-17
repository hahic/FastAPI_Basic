from typing import List, Set, Union
from pydantic import BaseModel


class Test(BaseModel):
    ADDR_GUNGU: Union[str, None] = None
    ADDR_SI: Union[str, None] = None
    ADDR_DONG: Union[str, None] = None
    ROAD_ADDR: Union[str, None] = None
    MBS_NAME: Union[str, None] = None
    MBS_NO: Union[int, None] = None
    MBS_TYIN_NAME: Union[str, None] = None
    INSTM_YN: Union[str, None] = None
    APPRNO: Union[int, None] = None
    SAL_AMNT: Union[int, None] = None
    SCK_SAL_YN: bool = False
    STO_BELNR_YN: Union[int, None] = None
    JIBUN_ADDR: Union[str, None] = None
    NEW_ZIPCODE: Union[int, None] = None
    SAL_DVSN_CODE: Union[int, None] = None
    MBS_TYIN_CODE: Union[int, None] = None
    SKU_RQST_NO: Union[str, None] = None
    APRV_DATE: Union[int, None] = None
    BIN_CODE: Union[int, None] = None
    BASE_DATE: Union[int, None] = None
