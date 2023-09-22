# HelloBench

HelloBench is a new Docker benchmark focused on container startup latency.

### HelloBench Images

This git repo just contains the benchmark harness than runs various Docker images; it does not contain the images themselves.  One (not recommended) way to fetch the images is by using the hello.py script to pull the images from the Docker Hub:

```./hello.py --registry= --op=pull --all```
#### pull
python2 ./hello.py --registry= --op=pull --all
#### run
python2 ./hello.py --registry= --op=run --all
#### tag
python2 ./hello.py --registry2=menguozi --op=tag --all
#### push
python2 ./hello.py --registry=menguozi --op=push --all


The advantage of the above command is that it will fetch all the latest HelloBench images.  The disadvantage is that we don't plan to keep the benchmark script in sync with the latest changes in the Docker Hub.  That means some of the images may become unavailable, or may change in a way that breaks the hello.py script.

A (typically) better way to get the images is to download a snapshot of the images that is known to work with the script.  This also allows comparisons with results from others who run the benchmark.  Such a snapshot of the images is available as a single [tar.gz](http://research.cs.wisc.edu/adsl/Software/hello-bench/reg-dir.tar.gz) at on the [ADSL Website](http://research.cs.wisc.edu/adsl/Software/hello-bench/) at the University of Wisconsin-Madison.

To start a Docker registry hosting the snapshot, extract "reg-dir" from the snapshot, and start a v2 registry using that directory for storage as follows:

```docker run -d -p 5000:5000 -v `pwd`/reg-dir:/tmp/registry-dev registry:2```

### Examples

TODO
