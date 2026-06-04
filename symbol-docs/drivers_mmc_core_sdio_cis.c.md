# drivers/mmc/core/sdio_cis.c

Subsystem: drivers/mmc

## Functions (11)

### cis_tpl_parse
- Return type: static int
- Signature: cis_tpl_parse(struct mmc_card * card,struct sdio_func * func,const char * tpl_descr,const struct cis_tpl * tpl,int tpl_count,unsigned char code,const unsigned char * buf,unsigned size)
- Line: 120

### cistpl_funce
- Return type: static int
- Signature: cistpl_funce(struct mmc_card * card,struct sdio_func * func,const unsigned char * buf,unsigned size)
- Line: 222

### cistpl_funce_common
- Return type: static int
- Signature: cistpl_funce_common(struct mmc_card * card,struct sdio_func * func,const unsigned char * buf,unsigned size)
- Line: 155

### cistpl_funce_func
- Return type: static int
- Signature: cistpl_funce_func(struct mmc_card * card,struct sdio_func * func,const unsigned char * buf,unsigned size)
- Line: 172

### cistpl_manfid
- Return type: static int
- Signature: cistpl_manfid(struct mmc_card * card,struct sdio_func * func,const unsigned char * buf,unsigned size)
- Line: 83

### cistpl_vers_1
- Return type: static int
- Signature: cistpl_vers_1(struct mmc_card * card,struct sdio_func * func,const unsigned char * buf,unsigned size)
- Line: 25

### sdio_free_common_cis
- Return type: void
- Signature: sdio_free_common_cis(struct mmc_card * card)
- Line: 383

### sdio_free_func_cis
- Return type: void
- Signature: sdio_free_func_cis(struct sdio_func * func)
- Line: 418

### sdio_read_cis
- Return type: static int
- Signature: sdio_read_cis(struct mmc_card * card,struct sdio_func * func)
- Line: 243

### sdio_read_common_cis
- Return type: int
- Signature: sdio_read_common_cis(struct mmc_card * card)
- Line: 378

### sdio_read_func_cis
- Return type: int
- Signature: sdio_read_func_cis(struct sdio_func * func)
- Line: 398

## Structs (1)

### cis_tpl
- Line: 114
- Members:
  - code: unsigned char
  - min_size: unsigned char
  - parse: tpl_parse_t *

## Typedefs (1)

- **tpl_parse_t** → int ()(struct mmc_card *,struct sdio_func *,const unsigned char *,unsigned) (line 111)

## Variables (4)

- static **cis_tpl_funce_list** : const struct cis_tpl[] (line 216)
- static **cis_tpl_list** : const struct cis_tpl[] (line 235)
- static **speed_unit** : const unsigned int[8] (line 107)
- static **speed_val** : const unsigned char[16] (line 105)

## Macros (2)

- **FMT**(type) (line 337)
- **SDIO_READ_CIS_TIMEOUT_MS** (line 23)
