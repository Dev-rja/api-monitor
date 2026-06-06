# API Reliability Monitor — SLA Report

> Last updated: **2026-06-06 11:09 UTC** &nbsp;|&nbsp; APIs monitored: **12** &nbsp;|&nbsp; Healthy: **6/12** &nbsp;|&nbsp; Avg uptime: **79.1%**

## SLA summary

| Status | API | Uptime | SLA compliance | Avg (ms) | Max (ms) | SLA threshold | Breaches |
|--------|-----|-------:|---------------:|---------:|---------:|--------------:|---------:|
| ❌ | `numbers_trivia` | 0.0% | 73.66% | 2824.9 | 10206.7 | 1000ms | 266/1010 |
| ❌ | `public_apis_list` | 0.0% | 99.6% | 125.7 | 4595.4 | 1500ms | 4/1010 |
| ❌ | `ipapi_check` | 75.74% | 99.9% | 156.8 | 4507.0 | 2500ms | 1/1010 |
| ❌ | `nasa_apod` | 77.52% | 56.44% | 2959.9 | 10565.8 | 2000ms | 440/1010 |
| ⚠️ | `rest_countries` | 98.51% | 98.22% | 355.6 | 10221.5 | 2500ms | 18/1010 |
| ⚠️ | `open_meteo_weather` | 98.91% | 96.93% | 703.6 | 14877.1 | 2000ms | 31/1010 |
| ✅ | `dog_ceo_random` | 99.5% | 95.84% | 579.3 | 10244.1 | 2500ms | 42/1010 |
| ✅ | `catfact_random` | 99.7% | 99.21% | 264.5 | 10080.2 | 3000ms | 8/1010 |
| ✅ | `coingecko_bitcoin` | 99.7% | 100.0% | 96.8 | 253.3 | 1500ms | 0/1010 |
| ✅ | `useless_fact` | 99.8% | 99.6% | 622.5 | 10229.6 | 2500ms | 4/1010 |
| ✅ | `agify_name` | 99.9% | 99.7% | 381.0 | 16112.2 | 2000ms | 3/1010 |
| ✅ | `jsonplaceholder_posts` | 100.0% | 99.8% | 223.0 | 3882.8 | 2000ms | 2/1010 |

## Consistently slow windows

These APIs exceeded their SLA threshold on average during these hours:

| API | Hour (UTC) | Avg (ms) | SLA breach rate |
|-----|-----------|----------:|----------------:|
| `nasa_apod` | 03:00 | 4611.9 | 78.95% |
| `nasa_apod` | 02:00 | 4606.1 | 62.5% |
| `numbers_trivia` | 03:00 | 4408.7 | 42.11% |
| `nasa_apod` | 17:00 | 3959.8 | 50.88% |
| `nasa_apod` | 11:00 | 3824.2 | 49.12% |
| `nasa_apod` | 09:00 | 3820.6 | 50.0% |
| `nasa_apod` | 05:00 | 3766.2 | 62.96% |
| `numbers_trivia` | 05:00 | 3541.5 | 33.33% |
| `numbers_trivia` | 10:00 | 3366.7 | 31.58% |
| `numbers_trivia` | 07:00 | 3340.4 | 31.25% |

---
_Generated automatically by [api-monitor](https://github.com/Dev-rja/api-monitor) via GitHub Actions + dbt._
