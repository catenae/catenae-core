#!/usr/bin/env python
# -*- coding: utf-8 -*-

from catenae import Link, Electron, errors
import time


class SourceLink(Link):
    def generator(self):
        try:
            instance_uid = self.instances_store['by_group']['catenae_middlelink'][0]
            self.logger.log(f'Invoking plus_two() from instance {self.uid}')
            result = self.jsonrpc_call(instance_uid, 'plus_two', kwargs={'number': 18})
            self.logger.log(f'result: {result}')
            assert result == 20

        except KeyError:
            pass

        except errors.RPCError:
            self.logger.log(level='exception')

        time.sleep(5)


if __name__ == "__main__":
    SourceLink().start()