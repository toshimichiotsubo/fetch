my $hhost = "http://loading.u-strasbg.fr/ITRF/CM";
my $home = $ENV{"HOME"};
my $hdir = $home . "/ftp/loading.u-strasbg.fr/ITRF/CM"; ##### to be altered
my $flist = "wget-strasbg.list";

my @llist = ( "ATMIB", "ATMMO", "ECCO", "ECCO2", "ERAhyd", "ERAin", "GLDAS", "GLORYS", "MERRA", "MERRA2_hyd");
#@llist = ("ATMIB");

open (IN, $flist);
my @buf = <IN>;
close (IN);

foreach $l (@llist) {
  $d = $hdir . "/" . $l;
  $ll = "merra2" if $l eq "MERRA2_hyd";
  $ll = lc $l;
  #print("cd $d");
  chdir($d);
  foreach $bb (@buf) {
    $b = $bb;
    chop ($b);
    my $h = $hhost . "/" . $l . "/" . $b . "." . $ll;
    system("wget -N $h");
    my $lf = $d . "/" . $b . "." . $ll;
    my $lf2 = $d . "/" . substr($b, 0, 4) . ".neu";
    system("mv $lf $lf2") if -f $lf;
  }
}
