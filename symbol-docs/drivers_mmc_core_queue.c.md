# drivers/mmc/core/queue.c

Subsystem: drivers/mmc

## Functions (23)

### __mmc_cqe_recovery_notifier
- Return type: static void
- Signature: __mmc_cqe_recovery_notifier(struct mmc_queue * mq)
- Line: 73

### mmc_alloc_disk
- Return type: static gendisk *
- Signature: mmc_alloc_disk(struct mmc_queue * mq,struct mmc_card * card,unsigned int features)
- Line: 351

### mmc_alloc_sg
- Return type: static scatterlist *
- Signature: mmc_alloc_sg(unsigned short sg_len,gfp_t gfp)
- Line: 166

### mmc_cleanup_queue
- Return type: void
- Signature: mmc_cleanup_queue(struct mmc_queue * mq)
- Line: 494

### mmc_cqe_can_dcmd
- Return type: static bool
- Signature: mmc_cqe_can_dcmd(struct mmc_host * host)
- Line: 38

### mmc_cqe_check_busy
- Return type: void
- Signature: mmc_cqe_check_busy(struct mmc_queue * mq)
- Line: 32

### mmc_cqe_dcmd_busy
- Return type: static bool
- Signature: mmc_cqe_dcmd_busy(struct mmc_queue * mq)
- Line: 26

### mmc_cqe_issue_type
- Return type: static mmc_issue_type
- Signature: mmc_cqe_issue_type(struct mmc_host * host,struct request * req)
- Line: 43

### mmc_cqe_recovery_notifier
- Return type: void
- Signature: mmc_cqe_recovery_notifier(struct mmc_request * mrq)
- Line: 81

### mmc_cqe_timed_out
- Return type: static blk_eh_timer_return
- Signature: mmc_cqe_timed_out(struct request * req)
- Line: 95

### mmc_get_max_segments
- Return type: static unsigned short
- Signature: mmc_get_max_segments(struct mmc_host * host)
- Line: 204

### mmc_init_queue
- Return type: gendisk *
- Signature: mmc_init_queue(struct mmc_queue * mq,struct mmc_card * card,unsigned int features)
- Line: 426

### mmc_issue_type
- Return type: mmc_issue_type
- Signature: mmc_issue_type(struct mmc_queue * mq,struct request * req)
- Line: 60

### mmc_merge_capable
- Return type: static bool
- Signature: mmc_merge_capable(struct mmc_host * host)
- Line: 410

### mmc_mq_exit_request
- Return type: static void
- Signature: mmc_mq_exit_request(struct blk_mq_tag_set * set,struct request * req,unsigned int hctx_idx)
- Line: 225

### mmc_mq_init_request
- Return type: static int
- Signature: mmc_mq_init_request(struct blk_mq_tag_set * set,struct request * req,unsigned int hctx_idx,unsigned int numa_node)
- Line: 210

### mmc_mq_queue_rq
- Return type: static blk_status_t
- Signature: mmc_mq_queue_rq(struct blk_mq_hw_ctx * hctx,const struct blk_mq_queue_data * bd)
- Line: 234

### mmc_mq_recovery_handler
- Return type: static void
- Signature: mmc_mq_recovery_handler(struct work_struct * work)
- Line: 136

### mmc_mq_timed_out
- Return type: static blk_eh_timer_return
- Signature: mmc_mq_timed_out(struct request * req)
- Line: 120

### mmc_queue_map_sg
- Return type: unsigned int
- Signature: mmc_queue_map_sg(struct mmc_queue * mq,struct mmc_queue_req * mqrq)
- Line: 527

### mmc_queue_resume
- Return type: void
- Signature: mmc_queue_resume(struct mmc_queue * mq)
- Line: 489

### mmc_queue_setup_discard
- Return type: static void
- Signature: mmc_queue_setup_discard(struct mmc_card * card,struct queue_limits * lim)
- Line: 177

### mmc_queue_suspend
- Return type: void
- Signature: mmc_queue_suspend(struct mmc_queue * mq)
- Line: 477

## Variables (1)

- static **mmc_mq_ops** : const struct blk_mq_ops (line 343)

## Macros (2)

- **MMC_DMA_MAP_MERGE_SEGMENTS** (line 24)
- **MMC_QUEUE_DEPTH** (line 416)
