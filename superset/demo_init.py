#
# Creates demo database, dashboard, and slices.
#
import json

from sqlalchemy import String, DateTime, Date, Float, BigInteger
from superset import app, db
from superset.models import core as models
from superset.connectors.connector_registry import ConnectorRegistry

Slice = models.Slice
Dash = models.Dashboard
TBL = ConnectorRegistry.sources[ 'table' ]
config = app.config

DEMO_DB_NAME = "demo"
demo_slices = []
demoDbUri = ""

openShiftApp = false

def getPostgresUri():
    if demoDbUri:
        return demoDbUri
        
    demoDbName = config.get( "POSTGRES_DATABASE" )
    demoDbUser = config.get( "POSTGRES_USERNAME" )
    demoDbPswd = config.get( "POSTGRES_PASSWORD" )

    if openShiftApp:
        osProjectName = config.get( "OPENSHIFT_PROJECT" )
        demoDbUri = "postgresql+psycopg2://" 
                    + demoDbUser 
                    + ":" 
                    + demoDbPswd 
                    + "@superset-demo-postgresql." 
                    + osProjectName 
                    + ".svc.cluster.local:5432/"
                    + demoDbName
    else:
        demoDbUri = "postgresql://" 
                    + demoDbUser
                    + "@172.18.0.2:5432/"
                    + demoDbName

    print( "Postgres URI: " + demoDbUri )
    return demoDbUri

def get_or_create_demo_db():
    dbobj = (
        db.session.query( models.Database )
                  .filter_by( database_name = DEMO_DB_NAME )
                  .first()
    )

    if not dbobj:
        dbobj = models.Database(database_name = DEMO_DB_NAME )
        dbobj.set_sqlalchemy_uri( getPostgresUri )
        dbobj.expose_in_sqllab = True
        dbobj.allow_run_sync = True
        db.session.add( dbobj )
        db.session.commit()

    return dbobj

def merge_slice( slc ):
    o = db.session.query( Slice ).filter_by( slice_name = slc.slice_name ).first()

    if o:
        db.session.delete( o )

    db.session.add( slc )
    db.session.commit()

#
# CAR_DATA table and slice
#
def create_car_data():
    print( "Creating CAR_DATA table and slice" )

    tbl_name = 'CAR_DATA'
    tbl = db.session.query( TBL ).filter_by( table_name = tbl_name ).first()
    
    if not tbl:
        tbl = TBL( table_name = tbl_name )
        tbl.description = "Car data for each route."
        tbl.database = get_or_create_demo_db()
        db.session.merge( tbl )
        db.session.commit()
        tbl.fetch_metadata()

    slc = Slice(
        slice_name = "CarData",
        viz_type = 'table',
        datasource_type = 'table',
        datasource_id = tbl.id,
    )

    demo_slices.append( slc.slice_name )
    merge_slice( slc )

#
# DRIVER table and slice
#
def create_driver():
    print( "Creating DRIVER table and slice" )

    tbl_name = 'DRIVER'
    tbl = db.session.query( TBL ).filter_by( table_name = tbl_name ).first()
    
    if not tbl:
        tbl = TBL( table_name = tbl_name )
        tbl.description = "A collection of drivers."
        tbl.database = get_or_create_demo_db()
        db.session.merge( tbl )
        db.session.commit()
        tbl.fetch_metadata()

    slc = Slice(
        slice_name = "Drivers",
        viz_type = 'table',
        datasource_type = 'table',
        datasource_id = tbl.id,
    )

    demo_slices.append( slc.slice_name )
    merge_slice( slc )

#
# DRIVER_OFFENSE table and slice
#
def create_driver_offenses():
    print( "Creating DRIVER_OFFENSE table and slice" )

    tbl_name = 'DRIVER_OFFENSE'
    tbl = db.session.query( TBL ).filter_by( table_name = tbl_name ).first()
    
    if not tbl:
        tbl = TBL( table_name = tbl_name )
        tbl.description = "A collection of driver traffic violations."
        tbl.database = get_or_create_demo_db()
        db.session.merge( tbl )
        db.session.commit()
        tbl.fetch_metadata()

    slc = Slice(
        slice_name = "DriverOffenses",
        viz_type = 'table',
        datasource_type = 'table',
        datasource_id = tbl.id,
    )

    demo_slices.append( slc.slice_name )
    merge_slice( slc )

#
# ROUTE table and slice
#
def create_route():
    print( "Creating ROUTE table and slice" )

    tbl_name = 'ROUTE'
    tbl = db.session.query( TBL ).filter_by( table_name = tbl_name ).first()
    
    if not tbl:
        tbl = TBL( table_name = tbl_name )
        tbl.description = "A collection of routes."
        tbl.database = get_or_create_demo_db()
        db.session.merge( tbl )
        db.session.commit()
        tbl.fetch_metadata()

    slc = Slice(
        slice_name = "Routes",
        viz_type = 'table',
        datasource_type = 'table',
        datasource_id = tbl.id,
    )

    demo_slices.append( slc.slice_name )
    merge_slice( slc )

#
# TRAFFIC_VIOLATION table and slice
#
def create_traffic_violation():
    print( "Creating TRAFFIC_VIOLATION table and slice" )

    tbl_name = 'TRAFFIC_VIOLATION'
    tbl = db.session.query( TBL ).filter_by( table_name = tbl_name ).first()
    
    if not tbl:
        tbl = TBL( table_name = tbl_name )
        tbl.description = "The collection of known traffic violations."
        tbl.database = get_or_create_demo_db()
        db.session.merge( tbl )
        db.session.commit()
        tbl.fetch_metadata()

    slc = Slice(
        slice_name = "TrafficViolations",
        viz_type = 'table',
        datasource_type = 'table',
        datasource_id = tbl.id,
    )

    demo_slices.append( slc.slice_name )
    merge_slice( slc )

#
# WEATHER_DATA table and slice
#
def create_weather_data():
    print( "Creating WEATHER_DATA table and slice" )

    tbl_name = 'WEATHER_DATA'
    tbl = db.session.query( TBL ).filter_by( table_name = tbl_name ).first()
    
    if not tbl:
        tbl = TBL( table_name = tbl_name )
        tbl.description = "Weather data for each route."
        tbl.database = get_or_create_demo_db()
        db.session.merge( tbl )
        db.session.commit()
        tbl.fetch_metadata()

    slc = Slice(
        slice_name = "WeatherData",
        viz_type = 'table',
        datasource_type = 'table',
        datasource_id = tbl.id,
    )

    demo_slices.append( slc.slice_name )
    merge_slice( slc )


def create_demo_dashboard():
    print( "Creating the demo dashboard" )

    db.session.expunge_all()
    DASH_SLUG = "superset_demo"
    dash = db.session.query( Dash ).filter_by( slug = DASH_SLUG ).first()

    if not dash:
        dash = Dash()
        dash.dashboard_title = "Superset Demo"
        dash.slug = DASH_SLUG
 
    js = textwrap.dedent("""\
    [
        {
            "col": 1,
            "row": 7,
            "size_x": 6,
            "size_y": 4,
            "slice_id": "442"
        },
        {
            "col": 1,
            "row": 2,
            "size_x": 6,
            "size_y": 5,
            "slice_id": "443"
        },
        {
            "col": 7,
            "row": 2,
            "size_x": 6,
            "size_y": 4,
            "slice_id": "444"
        },
        {
            "col": 9,
            "row": 0,
            "size_x": 4,
            "size_y": 2,
            "slice_id": "455"
        },
        {
            "col": 7,
            "row": 6,
            "size_x": 6,
            "size_y": 5,
            "slice_id": "467"
        },
        {
            "col": 1,
            "row": 0,
            "size_x": 8,
            "size_y": 2,
            "slice_id": "475"
        }
    ]
    """)

    l = json.loads( js )
    slices = (
        db.session.query( Slice )
                  .filter( Slice.slice_name.in_( demo_slices ) )
                  .all()
    )

    slices = sorted( slices, key = lambda x: x.id )

    for i, pos in enumerate( l ):
        pos[ 'slice_id' ] = str( slices[ i ].id )

    dash.position_json = json.dumps( l, indent = 4 )
    dash.slices = slices
    db.session.merge(d ash )
    db.session.commit()