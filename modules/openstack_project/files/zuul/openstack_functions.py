def set_log_url(item, job, params):
    if hasattr(item.change, 'refspec'):
        path = "%s/%s/%s/%s" % (
            params['ZUUL_CHANGE'][-2:], params['ZUUL_CHANGE'],
            params['ZUUL_PATCHSET'], params['ZUUL_PIPELINE'])
    elif hasattr(item.change, 'ref'):
        path = "%s/%s/%s" % (
            params['ZUUL_NEWREV'][:2], params['ZUUL_NEWREV'],
            params['ZUUL_PIPELINE'])
    else:
        path = params['ZUUL_PIPELINE']
    params['BASE_LOG_PATH'] = path
    params['LOG_PATH'] = path + '/%s/%s' % (job.name,
                                            params['ZUUL_UUID'][:7])
